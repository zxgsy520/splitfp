#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import gzip
import logging
import argparse

LOG = logging.getLogger(__name__)

__version__ = "2.2.3"
__author__ = ("Xingguo Zhang",)
__email__ = "invicoun@foxmail.com"
__all__ = []


def read_fasta(file):
    '''Read fasta file'''

    LOG.info("Reading message from %r" % file)
    if file.endswith(".gz"):
        fp = gzip.open(file)
    elif file.endswith(".fasta") or file.endswith(".fa"):
        fp = open(file)
    else:
        raise Exception("%r file format error" % file)

    seq = []
    for line in fp:
        if isinstance(line, bytes):
            line = line.decode('utf-8')
        line = line.strip().split()[0]
        if not line:
            continue
        if line.startswith(">"):
            if len(seq) == 2:
                yield seq
            seq = [line, ""]
        seq[1] += line
    if len(seq) == 2:
        yield seq
    fp.close()


def read_fastq(file):
    '''Read fastq file'''

    LOG.info("Reading message from %r" % file)
    if file.endswith("fastq.gz") or file.endswith(".fq.gz"):
        fp = gzip.open(file)
    elif file.endswith(".fastq") or file.endswith(".fq"):
        fp = open(file)
    else:
        raise Exception("%r file format error" % file)

    seq = []
    for line in fp:
        if isinstance(line, bytes):
            line = line.decode('utf-8')
        line = line.strip()

        if not line:
            continue
        if not seq:
            seq.append(line.split()[0])
            continue

        seq.append(line)
        if len(seq) == 4:
            yield seq
            seq = []

    fp.close()


def split_fp(reads, workdir, name, number, format='fastq', minlen=1000):

    n = 0
    lable = 1
    output = open('{}/{}.part_{}.{}'.format(workdir, name, lable, format), 'w')

    for i in reads:
        LOG.info('Read %s file' % i)
        if format=='fastq':
            fh = read_fastq(i)
        else:
            fh = read_fasta(i)

        for line in fh:
            seqlen = len(line[1])
            if seqlen < minlen:
                LOG.info("%s\t%s" % (line[0], seqlen))
                continue
            if n >= number:
                output.write("%s\n" % "\n".join(line))
                output.close()
                n = 0
                lable += 1
                output = open('{}/{}.part_{}.{}'.format(workdir, name, lable, format), 'w')

            output.write("%s\n" % "\n".join(line))
            n += 1

    output.close()


def split_data(read1, read2, workdir, name, number, minlen=1000):

    if not os.path.exists(workdir):
        os.makedirs(workdir)
    else:
        LOG.info('%s file exists' % workdir)

    if len(read1)!=len(read2) or not read2:
        name = name

        if read1[0].endswith(".fastq") or read1[0].endswith(".fq") or read1[0].endswith(".fastq.gz") or read1[0].endswith(".fq.gz"):
            format = 'fastq'
        else:
            format = 'fasta'

        split_fp(read1, workdir, name, number, format)

    else:
        format = 'fastq'
        name1 = name+'.r1'
        name2 = name+'.r2'

        if len(read1)==0:
            raise Exception('Can not find the input file, please check the input file format.')

        split_fp(read1, workdir, name1, number, format, minlen)
        split_fp(read2, workdir, name2, number, format, minlen)


def split_fq_help(parser):

    parser.add_argument('-r1', '--read1', metavar='FILE', nargs='+', type=str, required=True,
        help='Input R1 data, if it is three-generation sequencing, enter the reads sequence.')
    parser.add_argument('-r2', '--read2', metavar='FILE', nargs='+', type=str, default='',
        help='Input R2 data, not input if it is three-generation sequencing.')
    parser.add_argument('-w', '--workdir', metavar='FILE', type=str, default='.',
        help='Set the output file path, default=.')
    parser.add_argument('-n', '--number', metavar='INT', type=int, default=200000,
        help='Set the number of reads after splitting the file, default=200000')
    parser.add_argument('--minlen', metavar='INT', type=int, default=0,
        help='Filter the length of the sequence, default=0')
    parser.add_argument('-o', '--out', metavar='STR', type=str, default='out',
        help='Set the prefix of the output file.')

    return parser


def main():

    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
URL:https://github.com/zxgsy520/splitfp
name:
    splitfp  Split a specific format for multiple files.

attention:
    splitfp -r1 ngs.r1.fq -r2 ngs.r1.fq
    splitfp -r1 tgs.reads.fq
    splitfp -r1 tgs.reads.fq --minlen 1000
version: %s
contact:  %s <%s>\
        ''' % (__version__, ' '.join(__author__), __email__))

    args = split_fq_help(parser).parse_args()

    split_data(args.read1, args.read2, args.workdir, args.out, args.number, args.minlen)


if __name__ == "__main__":

    main()
