gunzip -c ../MCB185/data/dictionary.gz | grep "r" | grep -E "[zoniac]+" | grep -v -E "[qwetyupsdfghjklxvbm]" | grep -E ".{4,}"



