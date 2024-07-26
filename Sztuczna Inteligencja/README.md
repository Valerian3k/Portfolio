# Przykładowe rozwiązania w sztucznej inteligencji przy użyciu język Python
**1. Neuron Nieliniowy i Sieć Neuronowa:** Neuron Nieliniowy implementuje funkcje dla perceptronu: progowa_unipolarna() zwraca 1 lub 0 w zależności od wartości bloku sumującego, a sigmaidalna() oblicza funkcję sigmoidalną dla podanych wartości wejściowych; oba używają losowych wag. 
Sieć Neuronowa definiuje funkcję animal(), która klasyfikuje dane wejściowe (takie jak liczba nóg, środowisko życia, zdolność latania, itp.) do jednej z trzech kategorii: ssak, ptak lub ryba, używając predefiniowanych wag dla każdego typu gromady.

**2. Nauka Neuronu Nieliniowego:** implementuje algorytm perceptronu do uczenia maszynowego, który dostosowuje wagi w1, w2 i w3 na podstawie błędów w predykcjach dla zestawu danych wejściowych, aż do momentu, gdy wszystkie błędy są zminimalizowane, a liczba iteracji (kroków) procesu uczenia jest śledzona i wyświetlana.

**3. Sieć Hopfielda:** tworzy i stosuje macierz wag na podstawie wektora wejściowego x i wektora u1, a następnie oblicza wektor wyjściowy ex na podstawie wyniku sumowania iloczynów wag i wartości u1, przy czym wartości są przetwarzane na podstawie funkcji aktywacji.

**4. Propagacja Wsteczna:** implementuje sieć neuronową z jedną warstwą ukrytą, ucząc ją za pomocą algorytmu wstecznej propagacji błędów przy użyciu funkcji aktywacji sigmoidalnej, aktualizując wagi na podstawie obliczonych błędów i ich pochodnych przez określoną liczbę iteracji.

**5. Algorytm Genetyczny:** mplementuje algorytm genetyczny do optymalizacji współczynników wielomianu trzeciego stopnia, używając funkcji aktywacji jako kryterium dopasowania, obejmującego krzyżowanie, mutację, selekcję ruletkową oraz konwersję między postacią binarną a numeryczną, aby znaleźć najlepszy zestaw współczynników minimalizujący błąd funkcji na zadanym zbiorze danych.