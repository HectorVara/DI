package com.example.myothercatalog;
import android.app.Activity;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class LogoRecyclerViewAdapter extends RecyclerView.Adapter<LogoViewHolder> {
    private List<LogoData> allthedata;
    private Activity activity;

    public LogoRecyclerViewAdapter(List<LogoData> dataset, Activity activity){
        this.allthedata= dataset;
        this.activity= activity;
    }

    @NonNull
    @Override
    public LogoViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view= LayoutInflater.from(parent.getContext()).inflate(R.layout.logo_view_holder,
                parent,false);


        return new LogoViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull LogoViewHolder holder, int position) {
        LogoData dataInPositionToBeRendered= allthedata.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    @Override
    public int getItemCount() {
        return allthedata.size();
    }
}
