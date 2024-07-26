#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class Punkt2D {
public:
    double x, y;

    Punkt2D(double xp = 0, double yp = 0) : x(xp), y(yp)  {
        std::cout << "Stworzono punkt o wsp. " << x << ", " << y << std::endl;
    }

    Punkt2D(Punkt2D const& pkt) : x(pkt.x), y(pkt.y) {
        std::cout << "Stworzono punkt o wsp. " << x << ", " << y << std::endl;
    }

    double odleglosc(Punkt2D &pkt2) {
        return sqrt (pow(pkt2.x-x, 2) + pow(pkt2.y - y, 2) * 1.0);
    }

    void zmien_x(double nowy_x) {
        x = nowy_x;
    }

    ~Punkt2D() {
        std::cout << "Destruktor" << std::endl;
    }
};

class Kolo {
private:
    Punkt2D srodek;
    float promien;
public:

    Kolo()
    {
        srodek = Punkt2D(0,0);
        promien = 1;
    }

    Kolo(Punkt2D s = Punkt2D(0,0), float r = 1)
    {
        srodek = s;
        promien = r;
    }

    Kolo(int p1, int p2, float r = 1)
    {
        srodek = Punkt2D(p1,p2);
        promien = r;
    }

    Kolo(const Kolo &kolo)
    {
        srodek = kolo.srodek;
        promien = kolo.promien;
        cout << "konstruktor kopiujacy\n";
    }

    float Obw()
    {
        return 2 * 3.14 * promien;
    }

    float Pole()
    {
        return 3.14 * promien * promien;
    }

    ~Kolo() {
        std::cout << "Destruktor" << std::endl;
    }
};

int main()
{
    Kolo k1(Punkt2D(1,5), 4);
    Kolo k2(3, 6, 4);

    cout << "Obwod: " << k2.Obw() << " Pole: " << k2.Pole() << endl;

	return 0;
}


