gunzip -c "../MCB185/data/dictionary.gz" | grep r | grep -E "^[roznica]{4,}$" | wc -l
