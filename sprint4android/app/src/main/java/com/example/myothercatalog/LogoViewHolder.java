package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

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
    public LogoViewHolder(@NonNull View itemView) {
        super(itemView);
        context= itemView.getContext();
        descripcion= (TextView) itemView.findViewById(R.id.descripcion);
        imagen = (ImageView)  itemView.findViewById(R.id.imagen_logo);

    }
    public void showData(LogoData data, Activity activity){
        descripcion.setText(data.getDescrpcion());
        cancelPreviousImageDownloadIfAny();
        Util.downloadBitmapToImageView(data.getImageUrl(), this.imagen);
        imagen.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(view.getContext(), CatalogActivity.class);
                intent.putExtra("image_url",data.getImageUrl() );
                intent.putExtra("description", data.getDescrpcion());
            }
        });

    }

    private void cancelPreviousImageDownloadIfAny() {
    }
    private void loadImage(String imageUrl, Activity activity){}
    public Bitmap getBitMapFromUrl(String urlString) throws IOException {
        URL url=new URL(urlString);
        URLConnection connection=  url.openConnection();
        connection.connect();
        InputStream input= connection.getInputStream();
        Bitmap resultBipmap= BitmapFactory.decodeStream(input);
        return resultBipmap;
    }

}
