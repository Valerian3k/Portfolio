#include <iostream>

class Ulamek
{
private:
    double licznik;
    double mianownik;
public:
    Ulamek(double a = 0, double b = 0) : licznik(a), mianownik(b){};

    Ulamek & operator=(Ulamek & drugi)
    {
        if (this == &drugi)
            return *this;

        this->licznik = drugi.licznik;
        this->mianownik = drugi.mianownik;
        return *this;
    }

    Ulamek operator-()
    {
        Ulamek s;
        s.licznik = -(this->licznik);
        return s;
    };

    Ulamek operator*(const Ulamek &x1)
    {
        Ulamek s;
        s.licznik = this->licznik * x1.licznik;
        s.mianownik = this->mianownik * x1.mianownik;
        return s;
    }

    bool operator==(const Ulamek &x1)
    {
        return (this->licznik * x1.mianownik) == (x1.licznik * this->mianownik);
    }

    double& operator[](int i);

    friend Ulamek operator+(const Ulamek &x1, const Ulamek &x2);
    friend Ulamek operator*(const Ulamek &x, const int c);
    friend Ulamek operator*(const int c, const Ulamek &x);

    friend bool operator<=(const Ulamek &x1, const Ulamek &x2);
    friend bool operator<(const Ulamek &x1, const Ulamek &x2);
    friend bool operator>=(const Ulamek &x1, const Ulamek &x2);
    friend bool operator>(const Ulamek &x1, const Ulamek &x2);
    friend bool operator!=(const Ulamek &x1, const Ulamek &x2);

    friend std::ostream & operator<<(std::ostream &, Ulamek &);
    friend std::istream & operator>>(std::istream &, Ulamek &);

    operator double()
    {
        double x = licznik/mianownik;
        return x;
    }
};

Ulamek operator+(const Ulamek &x1, const Ulamek &x2)
{
    Ulamek s;
    s.licznik = (x1.licznik * x2.mianownik) + (x2.licznik * x1.mianownik);
    s.mianownik = x1.mianownik * x2.mianownik;
    return s;
}

Ulamek operator*(const Ulamek &x, const int c)
{
    Ulamek s;
    s.licznik = x.licznik * c;
    return s;
}

Ulamek operator*(const int c, const Ulamek &x)
{
    Ulamek s;
    s.licznik = c * x.licznik;
    return s;
}

bool operator<=(const Ulamek &x1, const Ulamek &x2)
{
    return (x1.licznik * x2.mianownik) <= (x2.licznik * x1.mianownik);
}

bool operator<(const Ulamek &x1, const Ulamek &x2)
{
    if ((x1.licznik * x2.mianownik) < (x2.licznik * x1.mianownik))
        return true;
    else
        return false;
}

bool operator>=(const Ulamek &x1, const Ulamek &x2)
{
    return (x1.licznik * x2.mianownik) >= (x2.licznik * x1.mianownik);
}

bool operator>(const Ulamek &x1, const Ulamek &x2)
{
    if ((x1.licznik * x2.mianownik) > (x2.licznik * x1.mianownik))
        return true;
    else
        return false;
}

bool operator!=(const Ulamek &x1, const Ulamek &x2)
{
	return (x1.licznik * x2.mianownik) != (x2.licznik * x1.mianownik);
}

double& Ulamek::operator[](int i)
{
    if (i < 0 || i > 1)
        throw std::out_of_range("Wrong index!");

    if (i == 0)
        return licznik;
    else
        return mianownik;
}

std::ostream & operator<<(std::ostream & wyjscie, Ulamek & x)
{
    wyjscie << "Zawartosc obiektu: " << x.licznik << "/" << x.mianownik;
    return wyjscie;
}

std::istream & operator>>(std::istream & wejscie, Ulamek & x)
{
    wejscie >> x.licznik >> x.mianownik;
    return wejscie;
}

int main()
{
    Ulamek x1(2, 4), x2(1, 2);

    if (x1 == x2)
        std::cout << "x1==x2" << std::endl;
    else if (x1 < x2)
        std::cout << "x1<x2" << std::endl;
    else if (x1 > x2)
        std::cout << "x1>x2" << std::endl;

    std::cout << "\nstd::cout << x1 << x2 << x3 \n";
    std::cout << x1 << " " << x2 << std::endl;

    std::cout << "\nOperator >> x1: \n";
    std::cin >> x1;
    std::cout << "\n" << x1;

    return 0;
}
