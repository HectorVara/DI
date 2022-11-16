package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private RequestQueue queue;
    private Context context= this;
    private LogoViewHolder viewHolder;
    private List<LogoData> listaLogos;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Runnable loadJson= new Runnable() {
            @Override
            public void run() {
                JsonArrayRequest request= new JsonArrayRequest(Request.Method.GET,
                        "https://raw.githubusercontent.com/HectorVara/DI/master/api-rest/catalog.json",
                        null,
                        new Response.Listener<JSONArray>(){
                            @Override
                            public void onResponse(JSONArray response) {
                                for (int i=0;i<response.length();i++){
                                    try {
                                        JSONObject logo= response.getJSONObject(i);
                                        LogoData unLogo= new LogoData(logo);
                                        listaLogos.add(unLogo);
                                        viewHolder.getBitMapFromUrl(unLogo.getImageUrl());
                                    } catch (JSONException e) {
                                        e.printStackTrace();
                                    } catch (IOException e) {
                                        e.printStackTrace();
                                    }
                                }

                            }
                        },
                        new Response.ErrorListener(){
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                if(error.networkResponse==null){
                                    Toast.makeText(context, "Server could not be reached", Toast.LENGTH_LONG).show();
                                }else{
                                    int serverCode=error.networkResponse.statusCode;
                                    Toast.makeText(context,"Server KO: "+serverCode, Toast.LENGTH_LONG).show();
                                }
                            }


                        });
                queue.add(request);

            }
        };
        Thread carga= new Thread(loadJson);
        carga.start();


    }
}