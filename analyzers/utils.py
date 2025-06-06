
def create_analyze_result(bbox, text, confidence, is_pass):
    return {
        "bbox": bbox,
        "text": text,
        "confidence": confidence,
        "pass": is_pass
    }
