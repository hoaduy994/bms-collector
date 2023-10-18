from flask import Flask, Response
import requests
import xml.etree.ElementTree as ET
import time
from dotenv import load_dotenv
import os
import subprocess

app = Flask(__name__)

@app.route("/api/xml", methods=["GET"])
def get_xml_data():
    xml_data = """<?xml version="1.0" encoding="UTF-8"?>
        <DoorData>
            <Door id="1">
                <Status>Open</Status>
                <Temperature>16</Temperature>
                <Voltage>220</Voltage>
                <PeopleIn>6</PeopleIn>
                <PeopleOut>2</PeopleOut>
                <TechnicalData>
                    <Width>90</Width>
                    <Height>210</Height>
                    <Material>Steel</Material>
                </TechnicalData>
            </Door>
            <Door id="2">
                <Status>Closed</Status>
                <Temperature>22</Temperature>
                <Voltage>220</Voltage>
                <PeopleIn>0</PeopleIn>
                <PeopleOut>1</PeopleOut>
                <TechnicalData>
                    <Width>80</Width>
                    <Height>200</Height>
                    <Material>Aluminum</Material>
                </TechnicalData>
            </Door>
            <Door id="3">
                <Status>Half-open</Status>
                <Temperature>23</Temperature>
                <Voltage>220</Voltage>
                <PeopleIn>3</PeopleIn>
                <PeopleOut>2</PeopleOut>
                <TechnicalData>
                    <Width>100</Width>
                    <Height>220</Height>
                    <Material>Glass</Material>
                </TechnicalData>
            </Door>
        </DoorData>
    """ 

    response = Response(response=xml_data, status=200, mimetype="application/xml")
    return response

if __name__ == "__main__":
    # subprocess.Popen(["python", "getdata.py"])
    app.run(host='0.0.0.0', port=5000)