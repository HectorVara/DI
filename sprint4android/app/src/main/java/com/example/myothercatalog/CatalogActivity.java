package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

public class CatalogActivity extends AppCompatActivity {
    private ImageView imagen;
    private TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);
        imagen= findViewById(R.id.imagen_logo);
        textView= findViewById(R.id.descripcion);
        Intent intent = getIntent();
        String url= getIntent().getExtras().getString("image_url");
        String description= getIntent().getExtras().getString("description");

        Util.downloadBitmapToImageView(url, this.imagen);
        textView.setText(description);
    }
}