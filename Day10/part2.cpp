#include<iostream>
#include<deque>
#include<vector>
#include<fstream>
#include <bits/stdc++.h>


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

void countdq(deque <char> g,long long& s1){
    deque <char> :: iterator it;
    for (it = g.begin(); it != g.end(); ++it){
        if(*it == '('){
            s1 = 5*s1+1;
            }
        else if(*it == '['){
            s1 = 5*s1+2;
            }
        else if(*it == '{'){
            s1 = 5*s1+3;
            }
        else if(*it == '<'){
            s1 = 5*s1+4;
            }
    }
}
int main(){    //part2:discard the corrupted lines. The remaining lines are incomplete.
    vector<string> inputs = readFile("part2day10.txt");
//    vector<string> inputs { "[({(<(())[]>[[{[]{<()<>>",
//                            "[(()[<>])]({[<{<<[]>>(",
//                            "{([(<{}[<>[]}>{[]{[(<()>",
//                            "(((({<>}<{<{<>}{[]{[]{}",
//                            "[[<[([]))<([[{}[[()]]]",
//                            "[{[{({}]{}}([{[{{{}}([]",
//                            "{<[[]]>}<{[{[{[]{()[[[]",
//                            "[<(<(<(<{}))><([]([]()",
//                            "<{([([[(<>()){}]>(<<{{",
//                            "<{([{{}}[<[[[<>{}]]]>[]]"};
    string open_bracket = "({[<";
    deque<char> de_que;
    vector<long long> counts;
    for(string s:inputs){
        long long s1 = 0;
        bool valid = true;
        for(char c:s){
            if(open_bracket.find(c) != string::npos) {
                de_que.push_front(c);
                }
            else if(c == ')'){
                if(de_que.front() != '('){
                    valid = false;
                    break;
                    }
                    de_que.pop_front();
                }
            else if(c == '}'){
                if(de_que.front() != '{'){
                    valid = false;
                    break;
                    }
                    de_que.pop_front();
                }
            else if(c == ']'){
                if(de_que.front() != '['){
                    valid = false;
                    break;
                    }
                    de_que.pop_front();
                }
            else if(c == '>'){
                if(de_que.front() != '<'){
                    valid = false;
                    break;
                    }
                    de_que.pop_front();
                }
        }
        if(valid){
            countdq(de_que,s1);
            counts.push_back(s1);
            }
        de_que.clear();
    }
    sort(counts.begin(),counts.end());
    cout<<"final answer: "<<counts.at(counts.size()/2)<<endl;
    return 0;
    }