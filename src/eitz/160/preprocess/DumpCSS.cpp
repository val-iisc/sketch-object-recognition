#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <stdlib.h>

// src_svg = SVG filepath corresponding to input sketch
// png_css_root_dir = Root directory where all temporally accumulated sketch sequences are to be stored as pngs
// svg_css_root_dir = Root directory where all temporally accumulated sketch sequences are to be stored as svgs
// category = Label name of category (e.g. "airplane")
// counter = Id of PNG or svg within the category directory (as per Eitz data layout) [1-80:airplane,81-160: ...]
int ProcessSVG(const string& src_svg,const char* png_css_root_dir,const char* svg_css_root_dir,const string& category,unsigned int counter)
{
	// Create destination category folders
	stringstream ss;
	// Create destination cateory directories
	ss << "mkdir -p \"" << png_css_root_dir << "/" << category << "/" << counter << "/" << "temporal\"";
	system(ss.str().c_str());
	ss.str("");
	ss << "mkdir -p \"" << svg_css_root_dir << "/" << category << "/" << counter << "/" << "temporal\"";
	system(ss.str().c_str());
	ss.str("");

	// Read svg file
	vector<string> svgLines;
	//cout << "SVG:" << src_svg << endl;
        ifstream ifs(src_svg.c_str());	
	string line;
	while (std::getline(ifs, line)) 
		svgLines.push_back(line);

	// Get indices of all lines containg stroke info(string 'path id')
	vector<unsigned int> strokeLineIds;
	string strk_token ="path id";
	for(unsigned int i = 0 ; i < svgLines.size() ; i++)
	{
		string line = svgLines.at(i);
		size_t found = line.find(strk_token);
		if (found != string::npos)
			strokeLineIds.push_back(i);
	}

        // Create a sequence of svgs/pngs where strokes are accumulated in cumultemporal order
        ss << png_css_root_dir << "/" << category << "/" << counter << "/" << "temporal";
        string dst_temporal_dir_png = ss.str();
        ss.str("");
        ss << svg_css_root_dir << "/" << category << "/" << counter << "/" << "temporal";
        string dst_temporal_dir_svg = ss.str();
        ss.str("");
        CreateCumulativeTemporalOrderSVG(svgLines,strokeLineIds,dst_temporal_dir_png,dst_temporal_dir_svg);

	return strokeLineIds.size();

}

void CreateCumulativeTemporalOrderSVG(const vector<string>& svgLines,const vector<unsigned int>& strokeLineIds,const string& dst_temporal_dir_png,const string& dst_temporal_dir_svg)
{
	unsigned int first_stroke_line_id = *min_element(strokeLineIds.begin(),strokeLineIds.end());
	unsigned int last_stroke_line_id  = *max_element(strokeLineIds.begin(),strokeLineIds.end());

	int counter = 1;
	stringstream ss;
	for(unsigned int i = first_stroke_line_id ; i <= last_stroke_line_id ; i++)
	{
		// Dump SVG
		ss << dst_temporal_dir_svg << "/" << counter << ".svg";
		string svg_path = ss.str();
		ofstream ofs_svg(ss.str().c_str());
		// Add lines up to and including i
		for(unsigned int j = 0 ; j <= i ; j++)
			ofs_svg << svgLines.at(j) << endl;
		// Add lines from last_stroke_line_id + 1 -> end
		for(unsigned int j = last_stroke_line_id + 1 ; j < svgLines.size() ; j++)
			ofs_svg << svgLines.at(j) << endl;
		ofs_svg.close();
		ss.str("");
		// Dump PNG
		ss << dst_temporal_dir_png << "/" << counter << ".png";
		string png_path = ss.str();
		ss.str("");
		ss << "convert -flatten -depth 8 -density 1200 -resize 256x256 \"" << svg_path << "\"  \"" << png_path << "\"";
		system(ss.str().c_str());
		ss.str("");

		++counter;
	}	
}
