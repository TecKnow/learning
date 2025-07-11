#include <cstdio>

enum class Operation{
    Add,
    Subtract,
    Multiply,
    Divide
};

struct Calculator{
    Calculator(Operation o){
        selected_operation = o;
    };

    int calculate(int first, int second){
        switch(selected_operation){
            case Operation::Add:{
                return first + second;
            } break;
            case Operation::Subtract:{
                return first - second;
            } break;
            case Operation::Multiply:{
                return first * second;
            } break;
            case Operation::Divide:{
                return first / second;
            } break;
        }
    }

    private:
    Operation selected_operation{};

};

int main(){
    int a{1}, b{2};
    Operation myOperation{Operation::Add};
    Calculator myCal{myOperation};
    printf("%d + %d is %d\n", a, b, myCal.calculate(a, b));


}