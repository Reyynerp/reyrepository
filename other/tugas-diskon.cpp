#include <iostream>
using namespace std;
int main() {
    double harga, harga_diskon;
    cout << "Masukkan harga orisinil: ";
    cin >> harga;
    if (harga < 100000) {
        harga_diskon = harga * (1 - 0.2);
    } else if (harga >= 100000 && harga < 200000) {
        harga_diskon = harga * (1 - 0.25);
    } else {
        harga_diskon = harga * (1 - 0.3);
    }
    cout << "Harga setelah diskon: Rp " << harga_diskon << endl;
    return 0;
}
