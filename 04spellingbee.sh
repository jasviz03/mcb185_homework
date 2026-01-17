gunzip -c dictionary.gz | grep  r | grep -E "^[roznica]{4,}$" | wc -l
