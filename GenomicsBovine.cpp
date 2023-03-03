#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n, m;
    ifstream in("cownomics.in");
    ofstream out("cownomics.out");
    in >> n >> m;
    string genomes[1000];
    for (int i = 0; i < 2 * n; i++) {
        string s;
        in >> s;
        genomes[i] = s;
    }
    int possible = 0;
    for (int i = 0; i < m; i++) {
        for (int j = i + 1; j < m; j++) {
            for (int k = j + 1; k < m; k++) {
                set<string> spotty;
                set<string> plain;
                for (int a = 0; a < n; a++) {
                    spotty.insert(genomes[a].substr(i, 1) + genomes[a].substr(j, 1) + genomes[a].substr(k, 1));
                }
                for (int b = n; b < 2 * n; b++) {
                    plain.insert(genomes[b].substr(i, 1) + genomes[b].substr(j, 1) + genomes[b].substr(k, 1));
                }
                int oldSizes = spotty.size() + plain.size();
                for (const string &str : plain) {
                    spotty.insert(str);
                }
                int newSize = spotty.size();
                if (newSize == oldSizes) {
                    possible++;
                }
            }
        }
    }
    out << possible << endl;
    return 0;
}