package com.example.myothercatalog;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

public class LogoViewHolder extends RecyclerView.ViewHolder {
    private TextView descripcion;
    private ImageView imagen;
    public LogoViewHolder(@NonNull View itemView) {
        super(itemView);
        descripcion= (TextView) itemView.findViewById(R.id.descripcion);
        imagen = (ImageView)  itemView.findViewById(R.id.imagen_logo);
    }
    public void showData(LogoData data, Activity activity){
        descripcion.setText(data.getDescrpcion());
        cancelPreviousImageDownloadIfAny();
        loadImage(data.getImageUrl(),activity);
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
