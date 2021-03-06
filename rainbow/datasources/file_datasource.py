#
# Copyright 2014 DoAT. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY DoAT ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL DoAT OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of DoAT

from base import DataSourceBase
from datasource_exceptions import InvalidDataSourceFormatException

__all__ = ['FileDataSource', 'File64DataSource']


class FileDataSource(DataSourceBase):
    datasource_name = 'file'

    def __init__(self, data_source):
        super(FileDataSource, self).__init__(data_source)

        if not ':' in data_source:
            raise InvalidDataSourceFormatException("FileDataSource must be in name:path_to_file format")

        name, path = data_source.split(':', 1)

        with open(path) as f:
            self.data = {name: f.read(-1)}


class File64DataSource(DataSourceBase):
    datasource_name = 'file64'

    def __init__(self, data_source):
        super(File64DataSource, self).__init__(data_source)

        if not ':' in data_source:
            raise InvalidDataSourceFormatException("File64DataSource must be in name:path_to_file format")

        name, path = data_source.split(':', 1)

        with open(path) as f:
            self.data = {name: f.read(-1).encode('base64')}
