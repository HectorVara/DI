package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class LogoData {
    private String descripcion;
    private String imageUrl;

    public LogoData(String descrpcion, String imageUrl) {
        this.descripcion = descrpcion;
        this.imageUrl = imageUrl;
    }

    public String getDescrpcion() {
        return descripcion;
    }

    public void setDescrpcion(String descrpcion) {
        this.descripcion = descrpcion;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }

    public LogoData(JSONObject json) throws JSONException {
        this.descripcion = json.getString("description");

        this.imageUrl=json.getString("image_url");
    }

}
