package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.app.AlertDialog;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

public class CatalogActivity extends AppCompatActivity {
    private ImageView imagen;
    private TextView textView;
    private AlertDialog.Builder myBuilder;
    private AlertDialog myDialog;

    Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);
        imagen = findViewById(R.id.imagen_logo);
        textView = findViewById(R.id.descripcion);
        //Con las tres siguientes líneas recogemos los datos que vienen en el Intent de la MainActivity
        Intent intent = getIntent();
        String url = getIntent().getExtras().getString("image_url");
        String description = getIntent().getExtras().getString("description");
        myBuilder = new AlertDialog.Builder(context);
        myBuilder.setView(inflateDialogView());
        myDialog = myBuilder.create();
        myDialog.show();

        Util.downloadBitmapToImageView(url, this.imagen);
        textView.setText(description);
        myDialog.dismiss();
    }
    private  View inflateDialogView() {
        LayoutInflater inflater = getLayoutInflater();
        View inflatedView = inflater.inflate(R.layout.loading, null);

        return inflatedView;
    }

}