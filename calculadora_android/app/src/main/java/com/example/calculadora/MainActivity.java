package com.example.calculadora;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private TextView screen;
    private Button AC, back, potencia, div, mult, minus, plus, equal, dot, one, two, three, four, five, six, seven, eight, nine, zero;
    private String input="", answer;
    Double result;

   //En la actividad simplemente se declaran los botones y se asocian con los del xml. No se les pone
    //el clicklistenner porque está en el botón del xml el atributo onclick asociado a una única función
    //Buttonclick

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        screen= findViewById(R.id.screen);
        AC= findViewById(R.id.ac);
        back= findViewById(R.id.back);
        potencia= findViewById(R.id.potencia);
        div= findViewById(R.id.division);
        mult= findViewById(R.id.multiplication);
        minus= findViewById(R.id.minus);
        plus= findViewById(R.id.plus);
        equal= findViewById(R.id.equal);
        dot= findViewById(R.id.dot);
        one= findViewById(R.id.one);
        two= findViewById(R.id.two);
        three= findViewById(R.id.three);
        four= findViewById(R.id.four);
        five= findViewById(R.id.five);
        six= findViewById(R.id.six);
        seven= findViewById(R.id.seven);
        eight= findViewById(R.id.eight);
        nine= findViewById(R.id.nine);
        zero= findViewById(R.id.zero);

    }
    //Con éste método le decimos a los botones y el textview cómo comportarse. El botón = será el
    //único que llame al método solve()
    public void ButtonClick(View view){
        Button button= (Button) view;
        String data= button.getText().toString();

        switch (data){
            case "AC":
                input="";
                break;
            case "←":
                if(input.length()>0) {
                    String deleted = input.substring(0, input.length() - 1);
                    input= deleted;
                }
                break;
            case "√":
                //La raiz cuadrada se muestra sin necesidad de pulsar la tecla =
                input=Double.toString(Math.sqrt(Double.parseDouble(input)));

            case "=":
                solve();

                break;
            default:
                if (data==null){
                    input="";
                }
                //Con este condicional se evita que se dupliquen los símbolos en la pantalla.
                //No es deseable tener un input 2++++2, por ejemplo
                if (data.equals("^") || data.equals("√") || data.equals("x") || data.equals("/") || data.equals("+") || data.equals("-")){
                    if(!input.matches(".*[x,\\/,+,\\-,^,√].*")){
                        System.out.println(input);
                        input+=data;
                    }
                }else{
                    input+=data;
                }

        //Para evitar que los números enteros salgan en la pantalla con el .0 al final
        }
        if(input.split("\\.").length==2){
            String decimal[]=input.split("\\.");
            if(decimal[1].equals("0")){
                input= decimal[0];
            }
        }

        screen.setText(input);
    }
    private void solve(){
        if(input.split("\\+").length==2){
            String[] op= input.split("\\+");
            result = Double.parseDouble(op[0]) + Double.parseDouble(op[1]);
            input= Double.toString(result);
        }
        if(input.split("\\-").length==2){
            String[] op= input.split("\\-");
            result = Double.parseDouble(op[0]) - Double.parseDouble(op[1]);
            input= Double.toString(result);
        }
        if(input.split("\\/").length==2){
            String[] op= input.split("\\/");
            result = Double.parseDouble(op[0]) / Double.parseDouble(op[1]);
            input= Double.toString(result);
        }
        if(input.split("x").length==2){
            String[] op= input.split("x");
            result = Double.parseDouble(op[0]) * Double.parseDouble(op[1]);
            input= Double.toString(result);
        }
        if(input.split("\\^").length==2){
            String[] op= input.split("\\^");
            result = Math.pow(Double.parseDouble(op[0]), Double.parseDouble(op[1]));
            input= Double.toString(result);
        }

    }
}