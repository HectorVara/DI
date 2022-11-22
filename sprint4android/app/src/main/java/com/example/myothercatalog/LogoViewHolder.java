package com.example.myothercatalog;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import android.view.LayoutInflater;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.List;

public class LogoViewHolder extends RecyclerView.ViewHolder {
    private TextView descripcion;
    private ImageView imagen;
    private Context context;
    private Bitmap bitmap;
    private View vista;
    private AlertDialog.Builder myBuilder;
    private AlertDialog myDialog;
    public LogoViewHolder(@NonNull View itemView) {
        super(itemView);
        context= itemView.getContext();
        descripcion= (TextView) itemView.findViewById(R.id.descripcion);
        imagen = (ImageView)  itemView.findViewById(R.id.imagen_logo);
        vista = (View) itemView.findViewById(R.id.holder);
        //La vista es holder, el constraintlayout de logo_view_holder.xml

    }

    public void showData(LogoData data, Activity activity){

        //Se muestran los datos y se coloca el listenner en la vista. Al pulsar imagen o descripción
        //se creará el Intent
        descripcion.setText(data.getDescrpcion());

        //La carga de la imagen en un hilo aparte y su inserción en el imageview están encapsuladas
        //en el método downloadBitmapToImageView de la clase Util
        Util.downloadBitmapToImageView(data.getImageUrl(), this.imagen);
        vista.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent intent = new Intent(view.getContext(), CatalogActivity.class);
                //Con putExtra le pasamos datos a CatalogActivity. Hay que acordarse de recogerlos
                //En el Oncreate de ésta
                intent.putExtra("image_url",data.getImageUrl() );
                intent.putExtra("description", data.getDescrpcion());
                view.getContext().startActivity(intent);

            }
        });



    }



}
