#include <iostream>

class Produkt
{
    std::string producent;
    std::string nazwa;
    int * cena;
public:
    Produkt(std::string producent, std::string nazwa, int cena)
    {
        this->producent = producent;
        this->nazwa = nazwa;
        this->cena = new int(cena);
    }

    //copy constructor
    Produkt(const Produkt & p)
    {
        this->producent = p.producent;
        this->nazwa = p.nazwa;
        this->cena = new int(*(p.cena));
    }

    // copy assignment operator
    Produkt& operator=(const Produkt& p)
    {
        if (this == &p)
            return *this;

        this->producent = p.producent;
        this->nazwa = p.nazwa;
        delete cena;
        this->cena = new int(*(p.cena));

        return *this;
    }

    void ustaw_cene(int nowa_cena)
    {
        if (nowa_cena >= 0)
        {
            *cena = nowa_cena;
        }
    }

    int zwroc_cene()
    {
        return *cena;
    }

    // destructor
    ~Produkt()
    {
        delete cena;
    }
};


int main()
{
    {
        Produkt myszka_rvm("Razer", "Viper Mini", 199);
        Produkt myszka_rvm_przecena(myszka_rvm);
        myszka_rvm_przecena.ustaw_cene(159);
        std::cout << "Cena Razer Viper Mini bez przeceny: " << myszka_rvm.zwroc_cene() << "\n";
        std::cout << "Cena Razer Viper Mini po przecenie: " << myszka_rvm_przecena.zwroc_cene() << "\n";
    }

    {
        Produkt myszka_lg100("Logitech", "G100", 1119);
        Produkt myszka_lg100s("Logitech", "G100s", 99);
        myszka_lg100 = myszka_lg100s;
        std::cout << "Cena Logotech G100: " << myszka_lg100.zwroc_cene() << "\n";
    }
}
