# Splitfp
Splitfp is a software that can split the second and third generation sequencing data.
## Installation
Installation method 1
<pre><code>
git clone https://github.com/zxgsy520/splitfp.git
cd splitfp
chmod 755 splitfp
</code></pre>

Installation method 2
<pre><code>
wget https://github.com/zxgsy520/splitfp/archive/v2.2.1.tar.gz
tar -zxvf v2.2.1.tar.gz
cd splitfp-2.2.1
chmod 755 splitfp
</code></pre>

## Instructions
<pre><code>
usage: splitfp [-h] -r1 FILE [FILE ...] [-r2 FILE [FILE ...]] [-w FILE] [-n INT] [-o STR]

name:
    splitfp.py  Split a specific format for multiple files.

attention:
    splitfp.py -r1 ngs.r1.fq -r2 ngs.r1.fq
    splitfp.py -r1 tgs.reads.fq

version: 2.2.1
contact:  Xingguo Zhang <113178210@qq.com>        

optional arguments:
  -h, --help            show this help message and exit
  -r1 FILE [FILE ...], --read1 FILE [FILE ...]
                        Input R1 data, if it is three-generation sequencing, enter the reads sequence.
  -r2 FILE [FILE ...], --read2 FILE [FILE ...]
                        Input R2 data, not input if it is three-generation sequencing.
  -w FILE, --workdir FILE
                        Set the output file path, default=.
  -n INT, --number INT  Set the number of reads after splitting the file, default=200000
  -o STR, --out STR     Set the prefix of the output file.
</code></pre>
