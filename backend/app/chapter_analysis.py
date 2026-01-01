import pandas as pd


def analyze_chapter_difficulty(df: pd.DataFrame) -> list:
   
    chapter_stats = df.groupby("chapter_order").agg(
        avg_score=("score", "mean"),
        avg_time_spent=("time_spent", "mean"),
        dropout_rate=("completed", lambda x: 1 - x.mean())
    ).reset_index()

    max_score = chapter_stats["avg_score"].max()
    max_time = chapter_stats["avg_time_spent"].max()

    chapter_difficulty = []

    for _, row in chapter_stats.iterrows():
        score_factor = 1 - (row["avg_score"] / max_score)
        time_factor = row["avg_time_spent"] / max_time
        dropout_factor = row["dropout_rate"]

        difficulty_index = round(
            (0.4 * score_factor) +
            (0.3 * time_factor) +
            (0.3 * dropout_factor),
            2
        )

        if difficulty_index >= 0.6:
            level = "HIGH"
        elif difficulty_index >= 0.4:
            level = "MEDIUM"
        else:
            level = "LOW"

        chapter_difficulty.append({
            "chapter_order": int(row["chapter_order"]),
            "avg_score": round(row["avg_score"], 2),
            "avg_time_spent": round(row["avg_time_spent"], 2),
            "dropout_rate": round(row["dropout_rate"], 2),
            "difficulty_index": difficulty_index,
            "difficulty_level": level
        })

    chapter_difficulty.sort(
        key=lambda x: x["difficulty_index"],
        reverse=True
    )

    return chapter_difficulty
