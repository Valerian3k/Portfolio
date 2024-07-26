#include <iostream>
#include <math.h>

class Figura
{
public:
    virtual double oblicz_pole() { return 0; }
};

class Trojkat : public Figura
{
    double a, b, c;
public:
    Trojkat(double a, double b, double c)
    {
        this->a = a;
        this->b = b;
        this->c = c;
    }

    double oblicz_pole()
    {
        double p = (a + b + c)/2;
        return sqrt(p * (p-a) * (p-b) * (p-c) );
    };
};

class Prostokat : public Figura
{
protected:
    double a, b;
public:
    Prostokat(double a, double b) : a(a), b(b) {};
    double oblicz_pole() { return a * b; };
};

class Kolo : public Figura
{
protected:
    double a;
public:
    Kolo(double a) : a(a) {};
    double oblicz_pole() { return 3.14 * a * a; };
};

double sumuj_pola(Figura * figury[], int size)
{
    double suma = 0;
    for(int i = 0; i < size; ++i)
        suma += figury[i]->oblicz_pole();

    return suma;
}

int main()
{
    Trojkat t1(2, 2, 2);
    Prostokat p1(3, 4);
    Kolo k1(2);

    Figura * figury[3];
    figury[0] = &p1;
    figury[1] = &t1;
    figury[2] = &k1;

    Figura * w1 = &p1;
    Figura * w2 = &t1;
    Figura * w3 = &k1;

    std::cout << "Pole Prostokata: " << p1.oblicz_pole() << "\n";
    std::cout << "Pole Trojkata: " << t1.oblicz_pole() << "\n";
    std::cout << "Pole Kola: " << k1.oblicz_pole() << "\n";

    std::cout << "\n";

    std::cout << "Funkcja sumujaca: " << sumuj_pola(figury, 3) << "\n";
    std::cout << "Wywolanie metod na obiektach: " << p1.oblicz_pole() + t1.oblicz_pole() << "\n";
    std::cout << "Wywolanie metod na wskaznikach: " << w1->oblicz_pole() + w2->oblicz_pole() << "\n";

    return 0;
}
