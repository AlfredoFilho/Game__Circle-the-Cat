import sys
from PIL import Image, ImageDraw

def compute_image(cat, blocks, exits) :
    
    im = Image.open("gameboard.png").convert("RGBA")
    
    draw = ImageDraw.Draw(im)

    for el in blocks :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5

        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.line([init_x+10, init_y+10, end_x-10, end_y-10],
                  fill = "red", width=6)
        draw.line([init_x+10,end_y-10, end_x-10, init_y+10],
                  fill = "red", width=6)                

    for el in exits :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5

        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "blue"
        )

    for el in [cat] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5

        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "black"
        )
        
    del draw
    return im


if __name__ == "__main__" :
    cat    = eval(sys.argv[1])
    blocks = eval(sys.argv[2])
    exits  = eval(sys.argv[3])
    
    #im = compute_image(cat, blocks, exits)
    #im.save("aux.png", "PNG")

    compute_image(cat, blocks, exits).save("configuration.png")
    
