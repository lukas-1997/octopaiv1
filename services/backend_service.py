import requests
import streamlit as st
from typing import Tuple, Dict, Any
import json

def send_to_backend(backend_url: str, meeting_url: str, host_name: str, transcripts: list) -> Tuple[bool, str]:
    """
    Send meeting data to the backend

    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        payload = {
            "url": meeting_url,
            "host_name": host_name,
            "transcript": transcripts
        }

        response = requests.post(
            f"{backend_url}/api/meeting",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        st.write(response)
        return True, "Success"
    except requests.exceptions.RequestException as e:
        return False, f"Error: {str(e)}\nPayload: {json.dumps(payload, indent=2)}"
