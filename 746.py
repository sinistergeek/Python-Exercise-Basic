from collections import defaultdict, Counter
palette = defaultdict(list)
for xy, rgb in pixel_iter(img):
    palette[rgb].append(xy)

w,h = img.size
print("Total pixels",w*h)
print("Total colors",len(palette))
