#include<iostream>
#include<deque>
#include<vector>
#include<fstream>
using namespace std;

vector<string> readFile(string filename){
    ifstream in_file{filename};
    string line;
    vector <string> inputs;
    while(!in_file.eof()){
        getline(in_file,line);
        inputs.push_back(line);
        }

    in_file.close();
    return inputs;
    }


void showdq(deque <char> g)
{
    deque <char> :: iterator it;
    for (it = g.begin(); it != g.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
}
int main(){
    vector<string> inputs = readFile("part1inputs.txt");
    string open_bracket = "({[<";
    int s1 = 0;
    deque<char> de_que;
    for(string s:inputs){
        for(char c:s){
            if(open_bracket.find(c) != string::npos) {
                de_que.push_front(c);
                }
            else if(c == ')'){
                if(de_que.front() != '('){
                    s1+=3;
                    break;
                    }
                de_que.pop_front();
                }
            else if(c == '}'){
                if(de_que.front() != '{'){
                    s1+=1197;
                    break;
                    }
                de_que.pop_front();
                }
            else if(c == ']'){
                if(de_que.front() != '['){
                    s1+=57;
                    break;
                    }
                de_que.pop_front();
                }
            else if(c == '>'){
                if(de_que.front() != '<'){
                    s1+=25137;
                    break;
                    }
                de_que.pop_front();
                }
            }
            de_que.clear();
        }
        cout<<s1<<endl;    // 390993
    return 0;
    }