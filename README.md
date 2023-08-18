It's probably important to note that this was kinda a perfect storm for me.
1. This is what I do. Data & process automation has been the focus of my career for the last 15 years. My undergrad was in applied mathematics, I currently manage data, analytics, and machine learning engineering teams.
2. I also love puzzles, and especially word puzzles (inveterate NYT crossword addict). This is not the first time I've scripted solutions to puzzles like this, I literally do it for fun.


# OCR Image Processing

I used the open-source GOCR package (http://jocr.sourceforge.net/) to turn screenshots of the word searches into text. I actually tried to use Google's Tesseract first (https://github.com/tesseract-ocr/tesseract), but it depends heavily on interpreting letters in context (as in, it looks for words, not just letters) so it balked at a grid of random letters.
GOCR helpfully allows you to use a local database and run supervised learning where it'll ask for help when it can't quite read something. Here's what the parsing process looks like for the first loan's puzzle

```
[12:21:44] jmatthew:grid_images/ $ gocr -p ../../gocr/ -i grid01.png -C ABCDEFGHIJKLMNOPQRSTUVWXYZ -m 167

# show box + environment
# show box     x=   29  234 d=  19  29 r= 1 0
# show pattern x=    4  232 d=  69  38 t= 1 1
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,< 
,,,,,,,,,,,,,,,,,,,,,,,,,.##################,,,,,,,,,,,,,,,,,,,,,,,,, -
,,,,,,,,,,,,,,,,,,,,,,,,,###################,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,.#################.,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,< 
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,........####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,.......#####.......,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,.#################.,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,.##################,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,.##################,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,.##################,,,,,,,,,,,,,,,,,,,,,,,,,<-
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,< 
The above pattern was not recognized.
Enter UTF8 char or string for above pattern. Leave empty if unsure.
Press RET at the end (ALT+RET to store into RAM only) : I

# show box + environment
# show box     x=   27  648 d=  25  30 r= 1 0
# show pattern x=    7  646 d=  65  40 t= 1 2
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,##############...........,,,,,,,,,,,,,,,,,,,,<-
,,,,,,,,,,,,,,,,,,,,##############...........,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.############............,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####................,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####................,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####................,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####................,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####................,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####................,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####............####,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####............####,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####............####,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....####............####,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.########################,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,#########################,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
The above pattern was not recognized.
Enter UTF8 char or string for above pattern. Leave empty if unsure.
Press RET at the end (ALT+RET to store into RAM only) : L

# show box + environment
# show box     x=  424  857 d=  26  30 r= 1 0
# show pattern x=  404  855 d=  66  37 t= 1 1
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,< 
,,,,,,,,,,,,,,,,,,,,.#########......#########.,,,,,,,,,,,,,,,,,,,, -
,,,,,,,,,,,,,,,,,,,,###########....###########,,,,,,,,,,,,,,,,,,,,< 
,,,,,,,,,,,,,,,,,,,,###########....###########,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.######............#####..,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..####..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,...###..............###...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,...####............####...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,...####............####...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,....####..........#####...,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,....#####........#####....,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,....######.....#######....,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,.....###############......,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,......##############......,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,........##########........,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,..........######..........,,,,,,,,,,,,,,,,,,,,<-
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,< 
The above pattern was not recognized.
Enter UTF8 char or string for above pattern. Leave empty if unsure.
Press RET at the end (ALT+RET to store into RAM only) : U
Y I V E T V V Y M T
W O R J T A J G H C
I B C G G N O T I S
Y C F P W P Y N V D
I K P M H U O D Z P
N B J M F T D S V E
L N O V R L W U P R
S U A A M O N E Y K
X P H A Q U F M N R
D W C R F V O C Z R
```

The long part of this was taking 49 screenshots from the PDF. I put them all in a folder and wrote a shell script to turn each one into text like the above, then take all the outputs and write them into a single file that could be read by the python script that solved the word searches.


# Puzzle Solver

Takes as input a puzzle in the form of a string of 100 letters, so the puzzle above becomes:
Y I V E T V V Y M T W O R J T A J G H C I B C G G N O T I S Y C F P W P Y N V D I K P M H U O D Z P N B J M F T D S V E L N O V R L W U P R S U A A M O N E Y K X P H A Q U F M N R D W C R F V O C Z R 

The process first converts that string of 100 characters into groups of strings to search for words. For each puzzle, that'd be ten rows, ten columns, nineteen left diagonals and nineteen right diagonals, and each one could be searched either forwards or backwards.
In code, I handled that as eight arrays of strings: horizontal, vertical, left and right diagonals, and all their respective reverses.
So for the puzzle above, those would be:
```
H=['YIVETVVYMT', 'WORJTAJGHC', 'IBCGGNOTIS', 'YCFPWPYNVD', 'IKPMHUODZP', 'NBJMFTDSVE', 'LNOVRLWUPR', 'SUAAMONEYK', 'XPHAQUFMNR', 'DWCRFVOCZR']
HR=['TMYVVTEVIY', 'CHGJATJROW', 'SITONGGCBI', 'DVNYPWPFCY', 'PZDOUHMPKI', 'EVSDTFMJBN', 'RPUWLRVONL', 'KYENOMAAUS', 'RNMFUQAHPX', 'RZCOVFRCWD']
V=['YWIYINLSXD', 'IOBCKBNUPW', 'VRCFPJOAHC', 'EJGPMMVAAR', 'TTGWHFRMQF', 'VANPUTLOUV', 'VJOYODWNFO', 'YGTNDSUEMC', 'MHIVZVPYNZ', 'TCSDPERKRR']
VR=['DXSLNIYIWY', 'WPUNBKCBOI', 'CHAOJPFCRV', 'RAAVMMPGJE', 'FQMRFHWGTT', 'VUOLTUPNAV', 'OFNWDOYOJV', 'CMEUSDNTGY', 'ZNYPVZVIHM', 'RRKREPDSCT']
DL=['Y', 'IW', 'VOI', 'ERBY', 'TJCCI', 'VTGFKN', 'VAGPPBL', 'YJNWMJNS', 'MGOPHMOUX', 'THTYUFVAPD', 'CINOTRAHW', 'SVDDLMAC', 'DZSWOQR', 'PVUNUF', 'EPEFV', 'RYMO', 'KNC', 'RZ', 'R']
DLR=['Y', 'WI', 'IOV', 'YBRE', 'ICCJT', 'NKFGTV', 'LBPPGAV', 'SNJMWNJY', 'XUOMHPOGM', 'DPAVFUYTHT', 'WHARTONIC', 'CAMLDDVS', 'RQOWSZD', 'FUNUVP', 'VFEPE', 'OMYR', 'CNK', 'ZR', 'R']
DR=['T', 'MC', 'YHS', 'VGID', 'VJTVP', 'TAONZE', 'ETNYDVR', 'VJGPOSPK', 'IRGWUDUYR', 'YOCPHTWENR', 'WBFMFLNMZ', 'ICPMROFC', 'YKJVMUO', 'IBOAQV', 'NNAAF', 'LUHR', 'SPC', 'XW', 'D']
DRR=['T', 'CM', 'SHY', 'DIGV', 'PVTJV', 'EZNOAT', 'RVDYNTE', 'KPSOPGJV', 'RYUDUWGRI', 'RNEWTHPCOY', 'ZMNLFMFBW', 'CFORMPCI', 'OUMVJKY', 'VQAOBI', 'FAANN', 'RHUL', 'CPS', 'WX', 'D']
```

When the process finds a word, it turns it into a list of the coordinates of the letters in the grid.
For each search direction, the easy part was finding the word if it existed -- just looking for a known substring.
The harder part was producing an auditable output -- something I could look at to verify that the algorithm did its job.
eg, in the puzzle above, the word "MONEY" is in the 8th row starting at column 5 and ending at column 9.
therefore the coordinates of the word money are [(8,5),(8,6),(8,7),(8,8),(8,9)]
Turning a found word into a set of coordinates is super easy for the rows and columns, there's a little more involved in the diagonals.

So then given a list of sets of coordinates for solutions, I can re-print the puzzle but only include the letters that are part of a found word.

This is the output of the process for any given puzzle:

```
Solving Wordsearch 1
Grid:
Y I V E T V V Y M T
W O R J T A J G H C
I B C G G N O T I S
Y C F P W P Y N V D
I K P M H U O D Z P
N B J M F T D S V E
L N O V R L W U P R
S U A A M O N E Y K
X P H A Q U F M N R
D W C R F V O C Z R
Found: 2
• • • • • • • • • •
• • • • • • • • • •
• • • • • • • • • •
• • • • • • • N • •
• • • • • • O • • •
• • • • • T • • • •
• • • • R • • • • •
• • • A M O N E Y •
• • H • • • • • • •
• W • • • • • • • •

For a slightly more complicated one:
Solving Wordsearch 48
Grid:
B K Y B O S T W K M
B U F E C L G H H Y
B H S H N X I A Z Y
E F O I E O U R M V
B O D L N G M T E E
L S R Q W E S O S L
E R U T U F S N U Z
Y R L K V W P S X Q
Y C H W E U N X K O
Y P Q B A Q T H G T
Found: 5
B • Y • • S • W • •
• U • E C • • H • •
• • S H N • • A • •
• • O I • O • R • •
• O • • N • M T • •
L • • • • E • O • •
E R U T U F S N • •
• • • • • • • S • •
• • • • • • • • • •
• • • • • • • • • •
```
