# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------------------------------
   File Name   :  process_xml.py
   Description :  处理xml为lab格式
   Run Script  :  python  process_xml.py
   Envs        : pip install xml2df
   Date        :  2021/7/24  下午12:39
   CodeStyle   :  standard, simple, readable, maintainable, and portable!
-------------------------------------------------------------------------
   Change Activity:
          2021/7/24 : build
-------------------------------------------------------------------------
__Author__ = "X-CCS 13026688597"
__Email__ = "CCS695146667@163.com"
__Copyright__ = ""
-------------------------------------------------------------------------
'''
import xml.etree.ElementTree as ET

def read_XML(xml_path):
    '''读取xml'''
    tree =  ET.parse(xml_path)
    root = tree.getroot()

    tempo_value = list(root.iter('sound'))[0].attrib['tempo']
    beat_time = 60/float(tempo_value)
    print('beat_time', beat_time, '\n--------')
    for part in root.iter('part'):
        for attribute in part.iter('attributes'):
            for divisions in attribute.iter('divisions'):
                print("divisions",divisions.text)
            for time in  attribute.iter('time'):
                for beats in time.iter("beats"):
                    beatstext = beats.text
                for beattype in time.iter("beat-type"):
                    beattypetext = beattype.text
                beat = beatstext+"/"+beattypetext
                print("节拍:",beat,"\n-------")
        noteTrue = False
        for note in part.iter('note'):
            for pitch in note.iter('step'):
                print('pitch',pitch.text)
                noteTrue = True

            for duration in note.iter('duration'):
                print('duration', duration.text)
            if noteTrue:
                for octave in note.iter('octave'):
                    print('octave', octave.text)

                for lyric in note.iter('text'):
                    print('text', lyric.text)
                noteTrue = False
                print('---------')

    xml_data = ""
    return xml_data

def xml2time_pitch_lyric(xml_path):
    '''将xml处理为time,音高,歌词'''
    xml_data = read_XML(xml_path)
    time_pitch_lyric = ""
    return time_pitch_lyric

if __name__ == "__main__":
    xml_path = "test.xml"
    time_pitch_lyric = xml2time_pitch_lyric(xml_path)


