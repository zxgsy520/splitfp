# Splitfp can mainly split multiple fastq or fasta files by the specified number of reads.
#Instructions
usage: splitfp [-h] -i FILE [-w FILE] [-n INT] [-o STR]

name:
    splitfp.py  Split a specific format for multiple files.

attention:
    splitfp.py -i fasta.list
    splitfp.py -i fasta.list -n 100000 -o name

version: 0.1.0
contact:  Xingguo Zhang <113178210@qq.com>        

optional arguments:
  -h, --help            show this help message and exit
  -i FILE, --input FILE
                        Set the input file.
  -w FILE, --workdir FILE
                        Set the output file path, default=.
  -n INT, --number INT  Set the number of reads after splitting the file,
                        default=200000
  -o STR, --out STR     Set the prefix of the output file.
