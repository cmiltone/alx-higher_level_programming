# script prints size of body of response in bytes
for arg in "$@"
do
url="$arg"
done
curl -s "$url" | wc -c