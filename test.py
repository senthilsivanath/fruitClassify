import base64

jpgtxt = open('test.jpg','rb').read().encode('base64').replace('\n','')
f = open("jpg1_b64.txt", "w")
f.write(jpgtxt)
f.close()

g = open("out.jpg", "w")
g.write(base64.decodestring(jpgtxt))
g.close()