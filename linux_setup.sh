# Set up a link for the program in the binary directory
BASHSTR="$(realpath $0)"
FP="$(dirname $BASHSTR)"
MAINFP="$FP/src/main.py"
echo $MAINFP
sudo ln -sf $MAINFP "/usr/bin/faa_eval"
chmod +x $MAINFP