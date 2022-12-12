package com.example.calculadora;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private TextView screen;
    private Button AC, back, percent, div, mult, minus, plus, equal, dot, one, two, three, four, five, six, seven, eight, nine, zero;
    private String input, answer;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        screen= findViewById(R.id.screen);
        AC= findViewById(R.id.ac);
        back= findViewById(R.id.back);
        percent= findViewById(R.id.percent);
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
}