import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    key = {}
    p = (1 - damping_factor)/len(corpus.keys())
    for i in corpus.keys():
        key[i] = p
    linkNum = len(corpus[page])
    if linkNum == 0:   #if no outgoing links, model returs p distribution that chooses equally aong all pages
        for i in corpus.keys():
            key[i] += damping_factor/len(corpus.keys())
        return key
    for i in corpus[page]:
        key[i] += damping_factor/linkNum
    return key
    # raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    key = {}
    for i in corpus.keys():
        key[i] = 0
    r = random.randint(0, len(corpus.keys())- 1)
    page = list(corpus.keys())[r]
    num = 0
    while num < n:
        key[page] += 1
        r = random.random()
        num += 1
        p = transition_model(corpus, page, damping_factor)
        for i in p.keys():
            if p[i] < r:
                r -= p[i]
            else:
                page = i
                break
    add = sum(key.values())
    for i in key.keys():
        key[i] = key[i] / add
    return key    
    # raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    rank = {}
    for i in corpus.keys():
        rank[i] = 1 / len(corpus.keys())

    temp = 1
    while temp:
        temp = 0
        tmp = {}
        for i in rank.keys():
            x = rank[i]
            tmp[i] = float((1-damping_factor) / len(corpus.keys()))
            for page, link in corpus.items():
                if i in link:
                    y = float(damping_factor*rank[page])
                    tmp[i] += y / len(link)
            if (x - tmp[i] > 0.001) or (tmp[i] - x > 0.001):
                temp = 1
        for i in rank.keys():
            rank[i] = tmp[i]
    return rank
   # raise NotImplementedError


if __name__ == "__main__":
    main()
