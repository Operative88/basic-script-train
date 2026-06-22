for plik in *.txt; do
    echo "Przetwarzam: $plik"
    wc -l "$plik"
done