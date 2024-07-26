A function is defined as: type function name(int param1 , float param2..){... return __; }
It has a return type and if not maintained, an error is generated at compile time.
A return statement in the function is compulsory. 
N number of parameters are allowed. A non-parameterized function is allowed too.
To call a function: name(param_name);
Nested functions are also allowed: eg: hello((hello("nivi","hey"), "world");
A global variable can be accessed inside a function but a local variable of function cannot be accessed outside its scope.
Closure of functions is also allowed, meaning a function's definition nested in another can access the variables of it's outside scope: eg:
  int function hi(){ 
    int b = 10;
    function test(){
      int c = b + 10;
      return c;
      }
    return b;
  }


  
