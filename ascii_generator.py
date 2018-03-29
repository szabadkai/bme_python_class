from PIL import Image

# image = Image.open('mysite/a49aea40-27e9-43d8-bbde-19c4af035b60.jpg')

class AsciiArt:
    def __init__(self, file_path, scale=" .:-=+*#%@"):
        self.image = Image.open(file_path)
        self.scale = scale

    def translate(self, pix):
        interval = 765//len(self.scale)
        intensity = sum(pix)
        return self.scale[int(intensity/interval)-1]

    def generate_art(self):
        art = []
        for i in range(0,self.image.height,15):
            for j in range(0,self.image.width,10):
                pix = self.image.getpixel((j,i))
                art.append(self.translate(pix))
            art.append('\n')
        print( ''.join(art))

        
if __name__ == "__main__"
    art=AsciiArt('mysite/a49aea40-27e9-43d8-bbde-19c4af035b60.jpg')
    art.generate_art()




