#!/usr/bin/env python3
"""
Problem  : Finding a Protein Motif
URL      : http://rosalind.info/problems/mprt/
Author   : David P. Perkins
"""

import urllib
import urllib.request

import regex


def read_fasta_url(url_str: str) -> (str, str,):
    s = urllib.request.urlopen(url_str).readall().decode()
    l = s.splitlines()
    protein_id = l[0].split('|')[1]
    protein_string = ''.join(l[1:])
    return protein_id, protein_string


def get_uniport_fasta_url(identifier: str):
    return 'http://www.uniprot.org/uniprot/{}.fasta'.format(identifier)


def uniprot_identifier_to_fasta(identifier: str):
    return read_fasta_url(get_uniport_fasta_url(identifier))


def motif_to_regex(motif_str: str):
    regex_string = motif_str.replace('{', '[^').replace('}', ']')
    regex_object = regex.compile(regex_string)
    return regex_object


def motif_matches(motif_str: str, protein_str: str):
    motif_regex = motif_to_regex(motif_str)
    return (x.start() for x in motif_regex.finditer(protein_str, overlapped=True))


def uniprot_identifiers_to_motif_matches(motif_str: str, uniprot_identifiers: [str]):
    fasta = ((x, uniprot_identifier_to_fasta(x)[1],) for x in uniprot_identifiers)
    return ((x[0], tuple(motif_matches(motif_str, x[1]))) for x in fasta)


def format_output(motif_matches):
    res_list = list()
    for x in motif_matches:
        if x[1]:
            res_list.append((x[0], tuple(y + 1 for y in x[1])))
    for x in res_list:
        print(x[0])
        print(*x[1])
    return res_list
