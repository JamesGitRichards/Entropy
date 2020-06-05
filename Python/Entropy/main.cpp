#include <stdio.h>

#include <iostream>

#include <conio.h>

#include <fstream>

#include <string>

#include <math.h>

using namespace std;

string alphabetta1 = "";

int N1;

int* p1;

string alphabetta2 = "";

int N2;

int* p2;

int n;

int n1;

int n2;

int** P;

int getIndex(char s, bool isFirst)

{

string alphabetta = "";

if (isFirst)

alphabetta = alphabetta1;

else

alphabetta = alphabetta2;

for (int i = 0; i < alphabetta.length(); i++)

{

char t = alphabetta[i];

if (s == t)

return i;

}

return -1;

}

void setAlphabetta(string text, bool isFirst)

{

int start = 1;

if (isFirst)

start = 0;

for (int i = start; i < n; i += 2)

{

int j = getIndex(text[i], isFirst);

if (j == -1)

{

if (isFirst)

alphabetta1 += text[i];

else

alphabetta2 += text[i];

}

}

}

void setP(string text)

{

N1 = alphabetta1.length();

N2 = alphabetta2.length();

p1 = new int[N1];

p2 = new int[N2];

int index;

for (int i = 0; i < N1; i++)

p1[i] = 0;

for (int i = 0; i < N2; i++)

p2[i] = 0;

for (int i = 0; i < n; i++) {

if (i%2 == 0)

{

index = getIndex(text[i], true);

if (index >= 0)

p1[index]++;

}

else

{

index = getIndex(text[i], false);

if (index >= 0)

p2[index]++;

}

}

//Условная вероятность

P = new int* [N1];

for (int i = 0; i < N1; i++)

P[i] = new int[N2];

for (int i = 0; i < N1; i++)

for (int j = 0; j < N2; j++)

P[i][j] = 0;

int _i;

int _j;

for (int i = 0; i < n - 1; i += 2) {

_i = getIndex(text[i], true);

_j = getIndex(text[i + 1], false);

P[_i][_j]++;

}

}

void entropy()

{

//энтропия первого источника

double sumShennon1 = 0;

double probability;

for (int i = 0; i < N1; i++)

{

probability = (double)p1[i] / (double)n1;

sumShennon1 += -1 * probability * log2(probability);

}

//энтропия второго

double sumShennon2 = 0;

for (int i = 0; i < N2; i++)

{

probability = (double)p2[i] / (double)n2;

sumShennon2 += -1 * probability * log2(probability);

}

cout << "H (независимые источники) = " << sumShennon1 + sumShennon2 << endl;

double Hx_Y = 0;

int nPairs = (double)n / 2;

for (int i = 0; i < N1; i++) {

double s = 0;

for (int j = 0; j < N2; j++) {

double p_i = (double)P[i][j] / nPairs;

p_i /= (p1[i]/(double)n1);

if (P[i][j] != 0)

s += -1*p_i * log2(p_i);

}

Hx_Y += ((double)p1[i]/(double)n1) * s;

}

double H = sumShennon1 + Hx_Y;

cout << "H = " << H << endl;

}

int main()

{

setlocale(LC_ALL, "rus");

string name = "Python/Entropy/1984.txt ";

string text;

string line;

ifstream input(name);

if (input.is_open())

while (!input.eof() )

{

getline(input,line);

text += line;

}

input.close();

n = text.length();

n1 = n / 2 + (n % 2);

n2 = n / 2;

setAlphabetta(text, true);

setAlphabetta(text, false);

setP(text);

entropy();

printf("\n\nPress any key...");

_getch();

return 0;

}