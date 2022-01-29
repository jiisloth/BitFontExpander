# BitFontExpander

BitFontExpander is a tool to expand or outline your pixel fonts.

Fonts are converted using BitFontMaker2

http://www.pentacom.jp/pentacom/bitfontmaker2

## How to fonts

1. Go to http://www.pentacom.jp/pentacom/bitfontmaker2
2. Create your own font or import your existing ttf font using "import ttf" button.
3. Use Data import/export button on the right corner of the character editor square.
4. Export your BitFontMaker2 data.
5. Use BitFontExpander to expand the font.
6. Import the expanded font data back to BitFontMaker2.
7. Build your font on BitFontMaker2. 

You might have to fiddle with the letterspacing. (Edit the "letterspace" value in the raw data for negative values.)

## Usage

running: 
```bash
python main.py
```

arguments:
```
main.py [-h] [-c N [X,Y ...]] [--middle {hollow,filled}] [-i INPUT] [-o OUTPUT] [{up,down,left,right,upleft,upright,downleft,downright,plus,round,widen,stretch}]

positional arguments:
  {up,down,left,right,upleft,upright,downleft,downright,plus,round,widen,stretch}
                        Choose way you want to expand font:
                        directionals: up, down, left, right
                        diagonals: upleft, upright, downleft, downright
                        Specials:
                        | plus  | round | widen |stretch|
                        |   X   |  XXX  |       |   X   |
                        |  XOX  |  XOX  |  XOX  |   O   |
                        |   X   |  XXX  |       |   X   |

optional arguments:
  -h, --help            show this help message and exit
  -c X,Y [X,Y ...], --custom X,Y [X,Y ...]
                        Pass offsets as pairs X1,Y1 X2,Y2. X grows righ, Y grows down,
  --middle {hollow,filled}
                        hollow: Removes the original bitmap from the result
                        filled: Adds the original bitmap to the result
  -i INPUT, --input INPUT
                        path for input file.
                        Default: ask for input.
  -o OUTPUT, --output OUTPUT
                        path for output file.
                        Default: print output
```
example:
```bash
python main.py round --input import.txt --output output.txt --middle hollow
```
converts char:
```
from:  to:
        ▇▇▇ 
  ▇    ▇▇ ▇▇
 ▇ ▇   ▇ ▇ ▇
 ▇▇▇   ▇   ▇
 ▇ ▇   ▇ ▇ ▇
       ▇▇▇▇▇
```

If you get errors when you paste the font data to BitFontExpander, try using a file.