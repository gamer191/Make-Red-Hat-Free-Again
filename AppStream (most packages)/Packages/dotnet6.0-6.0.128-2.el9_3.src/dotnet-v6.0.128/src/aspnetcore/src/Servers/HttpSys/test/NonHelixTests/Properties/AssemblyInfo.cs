﻿// Licensed to the .NET Foundation under one or more agreements.
// The .NET Foundation licenses this file to you under the MIT license.

using Microsoft.AspNetCore.Testing;
using Xunit;

[assembly: OSSkipCondition(OperatingSystems.MacOSX)]
[assembly: OSSkipCondition(OperatingSystems.Linux)]
[assembly: CollectionBehavior(DisableTestParallelization = true)]