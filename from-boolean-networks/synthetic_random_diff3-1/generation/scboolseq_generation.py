
def expand_bindata(traj_df, n_samples):
    d = traj_df.copy(deep=True).values.repeat(n_samples, axis=0)
    return pd.DataFrame(d, columns=traj_df.columns)

def make_counts(scb, bindata, prefix, SEED=SEED):
    for args, name in [({}, "normalized-scRNAseq-dropouts"), 
                       ({"dropout_mode": None}, "normalized-scRNAseq-nodropouts")]:
        counts = scb.sample_counts(bindata, n_samples_per_state=1, random_state=SEED)
        counts.index = [f"{x}_{y}" for i,x in enumerate(traj_df.index) for y in range(n_samples[i])]
        counts.index.name = "cellID"
        counts.T.to_csv(f"{output_prefix}traj/{prefix}-{name}.csv")
        sel = [i for i in counts.index if i.startswith("stable")]
        counts.loc[sel].T.to_csv(f"{output_prefix}steady/{prefix}-{name}.csv")
