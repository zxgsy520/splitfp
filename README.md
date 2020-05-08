# Splitfp
Splitfp is a software that can split the second and third generation sequencing data.
## Installation
Installation method 1
<pre><code>
git clone https://github.com/caonimademimi/splitfp.git
cd splitfp
chmod 755 splitfp
</code></pre>
Installation method 2
<pre><code>
wget https://github.com/caonimademimi/splitfp/blob/master/splitfp.tar.gz
tar -zxvf splitfp.tar.gz
cd splitfp 
chmod 755 -R * 
./splitfp -h
</code></pre>

## Instructions
<pre><code>usage: splitfp [-h] -i FILE [-w FILE] [-n INT] [-o STR] 

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
  ./splitfp -h
</code></pre>
