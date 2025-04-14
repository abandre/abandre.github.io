from PIL import Image
import urllib.request
import numpy as np

img = Image.open('unip.jpg') 

w,h = img.size


img_yuv = img.convert('YCbCr')

y, u, v = img_yuv.split()
y2 = y.resize((int(w/16),int(h/16)))
y2 = y2.resize((w,h))
u2 = u.resize((int(w/16),int(h/16)))
u2 = u2.resize((w,h))
v2 = v.resize((int(w/16),int(h/16)))
v2 = v2.resize((w,h))

img = Image.merge('YCbCr', (y2, u, v))
img.save("unip2.jpg")

# img_rgb = np.asarray(img)
# rgb_to_yuv = [[0.299,0.587,0.114],[-0.14713,-0.28886,0.436],[0.615,-0.51499,-0.10001]]

# img_yuv = np.zeros((h,w,3))
# print(img_yuv.shape)
# print(img_rgb.shape)

# for i in range(h):
#   for j in range(w):
#     img_yuv[i,j,:] = np.matmul(rgb_to_yuv,img_rgb[i,j,:])
    
# img = Image.fromarray(img_yuv.astype('uint8'), 'RGB')
# img.save("unip.png")

# print(np.asarray(img).shape)

# r, g, b = img.split()
# r2 = r.resize((int(w/16),int(h/16)))
# r2 = r2.resize((w,h))
# g2 = g.resize((int(w/16),int(h/16)))
# g2 = g2.resize((w,h))
# b2 = b.resize((int(w/16),int(h/16)))
# b2 = b2.resize((w,h))

# img = Image.merge('RGB', (r, g, b))
# img.save("unip.png")

# img = img.resize((int(w/16),int(h/16)))
# img = img.resize((w,h),Image.NEAREST) # Image.BILINEAR

# img.save("unip.png")
# im2.save("a.png")	

