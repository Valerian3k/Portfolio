#include <iostream>
#include <string>

using namespace std;

class Pracownik
{
private:
	string nazwisko;
protected:
	float stawka_godzinowa;
public:
	
    Pracownik(float st = 0, string naz = "brak")
    {
        nazwisko = naz;
        stawka_godzinowa = st;
    }

    float pensja(int liczba_godzin)
    {
        return stawka_godzinowa * liczba_godzin;
    }

    void wypisz()
    {
        cout << "Pracownik: " << nazwisko << " , stawka za godzine: " << stawka_godzinowa;
    }
};

class Stazysta : public Pracownik 
{
private:
	int dl_stazy_msc;
public:
	Stazysta(float st = 0, string naz = "brak", int ds = 0): Pracownik(st, naz), dl_stazy_msc(ds)
	{
		if(st > 15) Pracownik::stawka_godzinowa = 15;
	}
	
	void wypisz_msc() 
	{
		cout << " , miesiace stazu: " << dl_stazy_msc << endl;
	}
	
	void wypisz()
	{
		Pracownik::wypisz();
		wypisz_msc();
	}
};

int main()
{
/*	Pracownik pracownik1(16, "Kowalski");

	pracownik1.pensja(80);

	pracownik1.wypisz(); */
	
	{
		std::cout << "P:\n";
		Pracownik pracownik1(16, "Kowalski");
		pracownik1.wypisz();
	}

	std::cout << "\n";

	{
		std::cout << "S:\n";
		Stazysta stazysta1(18, "Nowak", 5);
		stazysta1.wypisz();
	}
	
	std::cout << "\n";

	return 0;
}

