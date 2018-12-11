#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os


class AntConan(ConanFile):
    name = "apache-ant"
    version = "1.10.5"
    url = "https://github.com/Tereius/conan-apache-ant"
    homepage = "https://ant.apache.org/index.html"
    description = "Apache Ant is a Java library and command-line tool whose mission is to drive processes described in build files as targets and extension points dependent upon each other."
    license = "https://www.apache.org/licenses/"
    build_requires = "java_installer/8.0.144@tereius/stable"
    settings = {"os_build": ["Windows", "Linux", "Macos"]}

    def source(self):
        source_url =\
            "http://mirror.dkd.de/apache//ant/binaries/apache-ant-%s-bin.zip" % self.version
        tools.get(source_url)

    def package(self):
        self.copy(pattern="*", src="apache-ant-%s" % self.version)

    def package_info(self):

        ant_root = self.package_folder
        self.output.info('Adding ant binaries to PATH: %s' % os.path.join(ant_root, "bin"))
        self.env_info.PATH.append(os.path.join(ant_root, "bin"))
