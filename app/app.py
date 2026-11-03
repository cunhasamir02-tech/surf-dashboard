import os
import time
import datetime
import threading
from flask import Flask, render_template, jsonify

app = Flask(__name__)
START_TIME = time.time()
_db_ready = False


def init_once():
    global _db_ready
    if _db_ready:
        return
    try:
        import surf_client as surf
        surf.init_db()
        _db_ready = True
    except Exception as exc:
        print(f"[WARN] init_db falhou: {exc}")


def refresh_bg():
    try:
        import surf_client as surf
        surf.refresh_all_spots()
    except Exception as exc:
        print(f"[WARN] refresh falhou: {exc}")


@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200


@app.route("/")
def dashboard():
    init_once()
    threading.Thread(target=refresh_bg, daemon=True).start()

    spots_list = []
    total_visits = 0

    try:
        import surf_client as surf
        surf.log_visit("/")
        spots = surf.get_all_spots()
        total_visits = surf.get_total_visits()
        for s in spots:
            d = dict(s)
            if d.get("fetched_at"):
                d["fetched_at"] = d["fetched_at"].strftime("%d/%m/%Y %H:%M")
            spots_list.append(d)
    except Exception as exc:
        print(f"[WARN] Erro ao buscar dados: {exc}")

    return render_template(
        "dashboard.html",
        spots=spots_list,
        total_visits=total_visits,
        uptime=int(time.time() - START_TIME),
        server_time=datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M UTC"),
    )


@app.route("/api/surf")
def api_surf():
    try:
        import surf_client as surf
        spots = surf.get_all_spots()
        return jsonify({"spots": [dict(s) for s in spots]})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/tides/<spot_id>")
def api_tides(spot_id):
    try:
        import surf_client as surf
        rows = surf.get_tide_data(spot_id)
        return jsonify({"spot_id": spot_id, "tides": [{"ts": str(r["ts"]), "height": r["tide_height"]} for r in rows]})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)import os
import time
import datetime
import threading
from flask import Flask, render_template, jsonify

app = Flask(__name__)
START_TIME = time.time()
_db_ready = False


def init_once():
    global _db_ready
    if _db_ready:
        return
    try:
        import surf_client as surf
        surf.init_db()
        _db_ready = True
    except Exception as exc:
        print(f"[WARN] init_db falhou: {exc}")


def refresh_bg():
    try:
        import surf_client as surf
        surf.refresh_all_spots()
    except Exception as exc:
        print(f"[WARN] refresh falhou: {exc}")


@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200


@app.route("/")
def dashboard():
    init_once()
    threading.Thread(target=refresh_bg, daemon=True).start()

    spots_list = []
    total_visits = 0

    try:
        import surf_client as surf
        surf.log_visit("/")
        spots = surf.get_all_spots()
        total_visits = surf.get_total_visits()
        for s in spots:
            d = dict(s)
            if d.get("fetched_at"):
                d["fetched_at"] = d["fetched_at"].strftime("%d/%m/%Y %H:%M")
            spots_list.append(d)
    except Exception as exc:
        print(f"[WARN] Erro ao buscar dados: {exc}")

    return render_template(
        "dashboard.html",
        spots=spots_list,
        total_visits=total_visits,
        uptime=int(time.time() - START_TIME),
        server_time=datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M UTC"),
    )


@app.route("/api/surf")
def api_surf():
    try:
        import surf_client as surf
        spots = surf.get_all_spots()
        return jsonify({"spots": [dict(s) for s in spots]})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/tides/<spot_id>")
def api_tides(spot_id):
    try:
        import surf_client as surf
        rows = surf.get_tide_data(spot_id)
        return jsonify({"spot_id": spot_id, "tides": [{"ts": str(r["ts"]), "height": r["tide_height"]} for r in rows]})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
