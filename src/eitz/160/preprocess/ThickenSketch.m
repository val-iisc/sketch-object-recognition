function I_thick = ThickenSketch(I)

% NOTE : If png images are 16-bit, convert them to 8-bit
% I = im2uint8(I);
se = strel('square',5);
I_thick = uint8(255)-uint8(imdilate(uint8(255)-uint8(I),se,'same'));

end
